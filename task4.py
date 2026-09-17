import segno

# Developer Profile Details
profile = """
================================
        DEVELOPER PROFILE
================================

Name: Raavi Rohith

Role: Python Full Stack Developer

Skills:
Python
SQL
HTML
CSS
JavaScript
React

Email:
raavi.rohit08@gmail.com

LinkedIn:
https://www.linkedin.com/in/raavi-rohith-44464b370/


GitHub:
https://github.com/raavirohit08-crypto

YouTube:
https://www.youtube.com/

Instagram:
https://www.instagram.com/

================================
        THANK YOU!
================================
"""

# Create QR Code
qr = segno.make(profile)

# Save QR Code
qr.save("developer_profile.png", scale=10)

print("Developer Profile QR Code Created Successfully!")
