import minify_html
import pathlib
import base64

extensions = {
  "securly_new": "chrome-extension://joflmkccibkooplaeoinecjbmdebglab/fonts/Metropolis.css",
  "securly_old": "chrome-extension://iheobagjkfklnlikgihanlhcddjoihkg/fonts/Metropolis.css",
  "goguardian": "chrome-extension://haldlgldplgnggkjaafhelgiaglafanh/youtube-injection.js"
}

base_path = pathlib.Path(__file__).resolve().parent
template_path = base_path / "template.html"
out_path = base_path / "generated"
template_html = template_path.read_text()

for name, url in extensions.items():
  html = template_html.replace("{{public_url}}", url)
  html = html.replace("{{extension_name}}", name)
  out_file = out_path / f"{name}.html"
  out_file.write_text(html)

  minified = minify_html.minify(html, minify_js=True, do_not_minify_doctype=True)
  html_encoded = base64.b64encode(minified.encode()).decode()
  data_url = f"data:text/html;base64,{html_encoded}"
  data_file = out_path / f"{name}_data_url.txt"
  data_file.write_text(data_url)