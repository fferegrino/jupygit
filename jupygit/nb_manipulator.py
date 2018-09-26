def clean_nb(dirty, outputs_to_remove=[]):
    cells = dirty.get('cells', [])
    to_remove = set(outputs_to_remove)
    for cell in cells:
        if cell["cell_type"] != "code": continue
        cell["execution_count"] = None
        if to_remove:  # WIP
            ix_to_remove = []
            for output in cell["outputs"]:
                if 'data' in output:
                    keys = output['data'].keys()
                    print(keys)
                elif 'name' in output:
                    print(output)
                else:
                    print(output)
        else:
            cell["outputs"] = []