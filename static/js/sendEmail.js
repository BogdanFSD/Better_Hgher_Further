


function sendEmail(contactForm) {
    
    emailjs.send("service_ia2pdsh", "Better",{
        "from_name":contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
        "request": contactForm.request.value
    })
    .then(
        function(response) {
            alert("SUCCESS", response);
        },
        function(error) {
            alert("FAILED", error);
        }
    );
    return false;
    }

