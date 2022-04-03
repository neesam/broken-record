let btn = document.querySelector('#review-btn');

let form = document.querySelector('form')

btn.addEventListener('click', () => {
  let textBox = document.createElement('textarea');

  textBox.id = 'textbox'
  textBox.name = 'content'

  textBox.style.height = '100px';
  textBox.style.width = '100%'
  textBox.style.marginTop = '50px'
  btn.style.display = 'none'

  tinymce.init({
    selector: 'textarea'
  })

  form.appendChild(textBox)
  
})