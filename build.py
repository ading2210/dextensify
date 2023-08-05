import minify_html
import pathlib
import base64

base_path = pathlib.Path(__file__).resolve().parent
template_path = base_path / "template.html"
out_path = base_path / "generated"

html = template_path.read_text()
out_file = out_path / f"main.html"
out_file.write_text(html)

minified = minify_html.minify(html, minify_js=True, do_not_minify_doctype=True, minify_css=True)
html_encoded = base64.b64encode(minified.encode()).decode()
data_url = f"data:text/html;base64,{html_encoded}"
data_file = out_path / "data_url.txt"
data_file.write_text(data_url)