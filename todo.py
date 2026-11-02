todos = [
    {"title": "レポートを提出する", "done": False, "priority": "高"},
    {"title": "教科書を返却する", "done": True, "priority": "中"},
]

print("TODO一覧")
print("状態と優先度：高・中・低")

print(f"すべてのTODO（{len(todos)}件）")

for todo in todos:
    if todo["done"]:
        status = "[完了]"
    else:
        status = "[未完了]"

    print(f"- {todo['title']} {status} [{todo['priority']}]")