def clean_nb(dirty, preserve=True):
    cells = dirty.get('cells', [])
    for cell in cells:
        if cell["cell_type"] != "code": continue
        cell["execution_count"] = None
        cell["outputs"] = []