console.log('hello world')
console.log('hello world')

// Array

copyBtns = [...document.getElementsByClassName('copy-btn')]
console.log(copyBtns)

let previous = null
let name = null


// Listen click on button
copyBtns.forEach(btn=> btn.addEventListener('click', ()=>{
        console.log('click')
        const copiedText = btn.getAttribute('copied-text')
        console.log(copiedText)
        navigator.clipboard.writeText(copiedText)
        btn.textContent = 'copied!'
        navigator.clipboard.readText().then(clipText => {
            console.log(clipText)
            btn.textContent = `Copied ${clipText} to clipboard!`
            name = clipText
        })

        if(previous){
            previous.textContent = name
        }

        previous = btn


    }
))