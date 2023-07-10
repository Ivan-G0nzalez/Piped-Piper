import jinja2
import pdfkit
from datetime import datetime

def created_report(data)-> None:
    now = datetime.now()
    timestamp_format = "%d-%m-%Y_%H-%M-%S"
    timestamp = now.strftime(timestamp_format)

    template_loader = jinja2.FileSystemLoader('./static/template/')
    template_env = jinja2.Environment(loader=template_loader)

    html_template = 'template_pdf.html'
    template = template_env.get_template(html_template)
    output_text = template.render(data)
    
    wkhtmlpdf_path = 'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'
    

    config = pdfkit.configuration(wkhtmltopdf=wkhtmlpdf_path)
    output_pdf = f"report/report_{timestamp}.pdf"
    pdfkit.from_string(output_text, output_pdf, configuration=config)


def created_report_perfomance(data)-> None:
    now = datetime.now()
    timestamp_format = "%d%m%Y%H%M%S"
    timestamp = now.strftime(timestamp_format)

    template_loader = jinja2.FileSystemLoader('./static/template/')
    template_env = jinja2.Environment(loader=template_loader)

    html_template = 'template_report_pdf.html'
    template = template_env.get_template(html_template)
    output_text = template.render(data)
    
    wkhtmlpdf_path = 'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'
    

    config = pdfkit.configuration(wkhtmltopdf=wkhtmlpdf_path)
    output_pdf = f"report/report_{timestamp}.pdf"
    pdfkit.from_string(output_text, output_pdf, configuration=config)