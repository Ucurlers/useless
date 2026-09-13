# === Stage 43: Добавь пагинацию длинных списков ===
# Project: SupportQueue
def paginate(items, page_size=20):
    total_pages = (len(items) + page_size - 1) // page_size if page_size else 1
    return {
        'total': len(items),
        'total_pages': total_pages,
        'page': 1,
        'page_size': page_size,
        'items': items[:page_size]
    }
