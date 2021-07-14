document.addEventListener('DOMContentLoaded', function() {
//     var miniinfo = document.getElementById('miniBio')
    
     getUserName()
//     var animatedText = document.getElementById('Typewriter')

    
});

    function getUserName() {
        const xhr = new XMLHttpRequest()
        const method = "GET"
        const url = `/user`
        const responseType = "json"
        xhr.responseType =responseType
        xhr.open(method, url)
        xhr.onload = function(){
            const serverResponse = xhr.response
            var currentUser = serverResponse.username
        // console.log(currentUser)
            userInformation(currentUser)
        }
        xhr.send()
    }

    function userInformation(username){
        const xhr = new XMLHttpRequest()
        const method = "GET"
        const url = `/api/${username}`
        const responseType = "json"
        xhr.responseType = responseType
        xhr.open(method, url)
        xhr.onload = function() {
            const serverResponse = xhr.response
            
            const fewWords = serverResponse.fewWords
            const information = serverResponse.information
            typewriterData(fewWords, information)
            informationData(information)
            const education = serverResponse.education
            const experience = serverResponse.experience
            const skillset = serverResponse.skillset
            const project = serverResponse.project
            console.log(education)
        }
        xhr.send()
    }

    function typewriterData(fewWords, information){
        var strings = [`${information.fullName}`]
        var i;
        for(i=0; i<fewWords.length;i++) {
            strings.push(`${fewWords[i].word}`)
        }
        var animatedText = document.getElementById('Typewriter')
        var typewriter = new Typewriter(animatedText, {
        strings,
        autoStart: true,
        loop: true,
        cursor: "|"
        });
        //console.log(strings, "Datatext")
    }

    function informationData(information){
        //console.log("Inforation: ", information)
        document.getElementById('myLinkedin').href = `${information.linkedin}`
        document.getElementById('myFacebook').href = `${information.facebook}`
        document.getElementById('myGithub').href = `${information.github}`
        document.getElementById('myInstagram').href = `${information.instagram}`
        document.getElementById('myTwitter').href = `${information.twitter}`
        var minibio = document.getElementById('home-bio')
        var about = document.getElementById('home-about')
        minibio.innerHTML = `${information.bio}`
        about.innerHTML = `${information.about}`
    }
