def unpack_entity(data, index_shift=False):
    shift = 1 if index_shift else 0
    return {
        "e_name": data[0 + shift],
        "e_number": float(data[1 + shift]),
        "e_date": data[2 + shift],
    }
