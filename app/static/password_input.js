window.addEventListener("load", function () {
    var checkbox = document.getElementById('check');
    var x = document.getElementById('password');
    checkbox.addEventListener('change', function () {
        if (this.checked) {
            x.type = 'text';
        } else {
            x.type = 'password';
        }
    });
});