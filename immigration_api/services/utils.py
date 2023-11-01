
# Convert Database result into dictionary
def row_to_dict(row, description):
    columns = [column[0] for column in description]
    results = []
    for data in row:
        results.append(dict(zip(columns, data)))
    return results


def one_row_to_dict(row, description):
    return dict(zip([t[0] for t in description], row))
