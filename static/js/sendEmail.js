


function sendEmail(contactForm) {
    
    emailjs.send("service_ia2pdsh", "Better",{
        "from_name":contactForm.name.value,
        "from_email": contactForm.email.value,
        "request": contactForm.request.value
    })
    .then(
        function(response) {
            alert("SUCCESS");
        },
        function(error) {
            alert("FAILED");
        }
    );
    return false;
    }

