def generate_rgb_tabs(results_dict):
    return [
        {"title": "Blue Channel", "image": results_dict["B"], "info": "B channel"},
        {"title": "Green Channel", "image": results_dict["G"], "info": "G channel"},
        {"title": "Red Channel", "image": results_dict["R"], "info": "R channel"}
    ]
