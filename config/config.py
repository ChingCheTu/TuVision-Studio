from modules.analysis.awb import run_awb_analysis
from modules.analysis.grayscale_analysis import run_grayscale_analysis
from modules.formatter.save import awb_save_format, grayscale_analysis_save_format
from modules.formatter.display import awb_display_format, grayscale_analysis_display_format

ANALYSIS_CONFIGS = {
    "AWB analysis": {
        "func": run_awb_analysis,
        "save_formatter": awb_save_format,
        "display_formatter": awb_display_format,
    },
    "Grayscale analysis": {
        "func": run_grayscale_analysis,
        "save_formatter": grayscale_analysis_save_format,
        "display_formatter": grayscale_analysis_display_format,
    }    
}