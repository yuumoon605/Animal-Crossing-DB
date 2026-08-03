from flask import Flask, render_template, request
from database import CREATURES_DATA

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
  # 検索・絞り込みフォームからの入力を取得
  search_query = request.args.get("q", "").strip()
  category_filter = request.args.get("category", "")
  min_price = request.args.get("min_price", type=int)
  season_filter = request.args.get("season", "")

  results = CREATURES_DATA

  # 名前検索（部分一致）
  if search_query:
    results = [
        item for item in results if search_query in item["name"]
    ]

  # カテゴリ絞り込み
  if category_filter:
    results = [
        item for item in results if item["category"] == category_filter
    ]

  # 価格（最低価格以上）での絞り込み
  if min_price is not None:
    results = [item for item in results if item["price"] >= min_price]

  # 出現時期での絞り込み（部分一致）
  if season_filter:
    results = [
        item for item in results
        if season_filter in item["season"].replace("月", "") or item["season"] == "通年"
    ]


  return render_template(
      "index.html",
      creatures=results,
      search_query=search_query,
      category_filter=category_filter,
      min_price=min_price if min_price is not None else "",
      season_filter=season_filter,
  )


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000)