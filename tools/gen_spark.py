# -*- coding: utf-8 -*-
"""
Sinh lưới biểu đồ SVG (sparkline) 1 tháng cho các mã cổ phiếu Nhật, kèm link TradingView.
Dữ liệu giá lấy từ Yahoo Finance (mã dạng <code>.T).

CÁCH DÙNG:
  python tools/gen_spark.py <file_output.html> "<code>:<tên_JP>:<%thay_đổi>:<up|down>" [...]

VÍ DỤ:
  python tools/gen_spark.py out.html "4812:電通総研:+14,71%:up" "9793:ダイセキ:-6,45%:down"

Kết quả: file HTML chứa <div class="spark-grid">…</div> — dán thẳng vào phần 2 của
archive/<TODAY>.html. Các class (spark-grid, spark-card, spark-cap, spark, spark-foot,
tv-link, up, down) đã được định nghĩa sẵn trong index.html.
"""
import json, sys, urllib.request


def fetch_closes(code):
    url = "https://query1.finance.yahoo.com/v8/finance/chart/%s.T?range=1mo&interval=1d" % code
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=15) as r:
        data = json.load(r)
    res = data["chart"]["result"][0]
    closes = res["indicators"]["quote"][0]["close"]
    return [c for c in closes if c is not None]


def make_svg(closes):
    W, H, PAD = 300.0, 80.0, 8.0
    n = len(closes)
    lo, hi = min(closes), max(closes)
    rng = (hi - lo) or 1.0
    pts = []
    for i, c in enumerate(closes):
        x = PAD + (W - 2 * PAD) * (i / (n - 1 if n > 1 else 1))
        y = PAD + (H - 2 * PAD) * (1 - (c - lo) / rng)
        pts.append((round(x, 1), round(y, 1)))
    trend_up = closes[-1] >= closes[0]
    stroke = "#17914e" if trend_up else "#c0392b"
    fill = "rgba(23,145,78,.10)" if trend_up else "rgba(192,57,43,.10)"
    line_pts = " ".join("%s,%s" % p for p in pts)
    area_pts = "%s,%s " % (pts[0][0], H - PAD) + line_pts + " %s,%s" % (pts[-1][0], H - PAD)
    lx, ly = pts[-1]
    return (
        '<svg class="spark" viewBox="0 0 300 80" preserveAspectRatio="none" xmlns="http://www.w3.org/2000/svg">'
        '<polygon points="%s" fill="%s" stroke="none"/>'
        '<polyline points="%s" fill="none" stroke="%s" stroke-width="2" stroke-linejoin="round" stroke-linecap="round"/>'
        '<circle cx="%s" cy="%s" r="3" fill="%s"/>'
        '</svg>'
    ) % (area_pts, fill, line_pts, stroke, lx, ly, stroke)


def build_card(code, name, chg, cls):
    try:
        closes = fetch_closes(code)
        svg = make_svg(closes)
        last_lbl = "¥" + "{:,}".format(int(round(closes[-1]))).replace(",", ".")
    except Exception as e:
        svg = '<div class="spark-err">Không tải được biểu đồ (%s)</div>' % e
        last_lbl = "—"
    tv_url = "https://www.tradingview.com/symbols/TSE-%s/" % code
    return (
        '  <div class="spark-card">\n'
        '    <div class="spark-cap"><b>%s %s</b><span class="%s">%s</span></div>\n'
        '    %s\n'
        '    <div class="spark-foot">%s · 1 tháng'
        '<a class="tv-link" href="%s" target="_blank" rel="noopener">TradingView ↗</a></div>\n'
        '  </div>' % (code, name, cls, chg, svg, last_lbl, tv_url)
    )


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        sys.exit(1)
    out_path = sys.argv[1]
    cards = []
    for spec in sys.argv[2:]:
        parts = spec.split(":")
        if len(parts) != 4:
            print("Bỏ qua đối số sai định dạng:", spec)
            continue
        code, name, chg, cls = parts
        cards.append(build_card(code.strip(), name.strip(), chg.strip(), cls.strip()))
    out = '<div class="spark-grid">\n' + "\n".join(cards) + "\n</div>\n"
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(out)
    print("Wrote %d chart(s) to %s (%d bytes)" % (len(cards), out_path, len(out)))


if __name__ == "__main__":
    main()
