


function sendEmail(contactForm) {
    emailjs.init("PnNIz_5JC9qfsENAO");
    emailjs.send("service_ia2pdsh", "Better",{
        "from_name":contactForm.name.value,
        "from_email": contactForm.emailaddress.value,
        "request": contactForm.projectsummary.value
    })
    .then(
        function (response) {
			console.log("SUCCESS", response);
		},
		function (error) {
			console.log('Failed to send', error); 
			failed();
		}
	);
    return false;
    }

