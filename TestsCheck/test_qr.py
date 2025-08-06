from qrstyler import QRGenerator
from qrstyler.themes import THEMES_DICT,  ThemesEnum

from qrstyler.generator import QRConfig




config = QRConfig(
    version=4,
    show_logo=True,
    show_theme=True,
    theme=ThemesEnum.INSTAGRAM,
    color_positiond_detection_corners=True,
    custom_finder_pattern_color="#E66030",
    custom_theme_color="#987FEA",
)
qrgen = QRGenerator(config)
qrgen.generate_qr_code("https://instagram.com/vipulm124", output_file="instagram_qr.png")


output_file = "qr_code_anotherone_saved.png"
default_config = QRConfig(version=4, show_logo=True, theme=ThemesEnum.WHATSAPP, show_theme=False, color_positiond_detection_corners=True, custom_finder_pattern_color="#96CC38")
qrcode_generator = QRGenerator(default_config)
qrcode_ready_to_save = qrcode_generator.generate_qr_code("https://www.marvel.com", output_file=output_file)
if qrcode_ready_to_save is not None:
    qrcode_ready_to_save.save(output_file)