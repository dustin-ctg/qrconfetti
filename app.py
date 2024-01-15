from flask import Flask, render_template, request, send_file
import qrcode
from io import BytesIO

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        
        if ( request.form.get('qr_code_type') == 'business_card' ):
            # Retrieve data from form
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            title = request.form.get('title')
            company = request.form.get('company')
            email = request.form.get('email')
            phone = request.form.get('phone')
            data = f"BEGIN:VCARD\nVERSION:3.0\nFN:{first_name} {last_name}\nN:{last_name};{first_name};;\nTITLE:{title}\nORG:{company}\nEMAIL:{email}\nTEL:{phone}\nEND:VCARD"
        elif (request.form.get('qr_code_type') == 'url'):
            url = request.form.get('url')
            data = f"{url}"
        else:
            return render_template('index.html')

        # Generate QR code
        
        qr = qrcode.QRCode(
            version=3,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)
        # request.form.get('qr_code_color')
        img = qr.make_image(fill_color=request.form.get('qr_code_color'), back_color="transparent")

        # Save image to a BytesIO object
        img_bytes = BytesIO()
        img.save(img_bytes)
        img_bytes.seek(0)

        return send_file(img_bytes, mimetype='image/png', as_attachment=True, download_name='qr_code.png')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(host="qrconfetti.celebrationtitlegroup.com")
