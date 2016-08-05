jQuery(function($) {

    if (typeof CodeMirror != 'undefined') {

        var codeMirror = CodeMirror.fromTextArea(document.getElementById('id_content'), {
            mode: 'htmlmixed',
            lineNumbers: true,
            theme: 'default'
        });
    }

});
