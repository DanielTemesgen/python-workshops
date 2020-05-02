from IPython.display import HTML, display

def hide_warnings():
    
    x = HTML('''<script>
    var code_show_err = false; 
    var code_toggle_err = function() {
     var stderrNodes = document.querySelectorAll('[data-mime-type="application/vnd.jupyter.stderr"]')
     var stderr = Array.from(stderrNodes)
     if (code_show_err){
         stderr.forEach(ele => ele.style.display = 'block');
     } else {
         stderr.forEach(ele => ele.style.display = 'none');
     }
     code_show_err = !code_show_err
    } 
    document.addEventListener('DOMContentLoaded', code_toggle_err);
    </script>
    To toggle on/off output_stderr, click <a onclick="javascript:code_toggle_err()">here</a>.''')
    
    display(x)