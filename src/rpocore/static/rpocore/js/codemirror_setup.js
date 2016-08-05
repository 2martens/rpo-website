jQuery(function($) {

    if (typeof CodeMirror != 'undefined') {

        var textareas = document.getElementsByClassName('codemirrorEditor');
        for (let textarea of textareas)
        {
            var codeMirror = CodeMirror.fromTextArea(textarea, {
                mode: 'htmlmixed',
                lineNumbers: true,
                theme: 'default'
            });
        }
    }
});
