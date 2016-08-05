from django import forms
from mezzanine.utils.static import static_lazy as static


class CodemirrorWidget(forms.Textarea):
    """
    Setup the JS files and targetting CSS class for a textarea to
    use Codemirror.
    """

    class Media:
        js = (static("rpocore/codemirror/lib/codemirror.js"),
              static("rpocore/codemirror/mode/css/css.js"),
              static("rpocore/codemirror/mode/javascript/javascript.js"),
              static("rpocore/codemirror/mode/xml/xml.js"),
              static("rpocore/codemirror/mode/htmlmixed/htmlmixed.js"),
              static("rpocore/js/codemirror_setup.js"))
        css = {'all': (static("rpocore/codemirror/lib/codemirror.css"),)}

    def __init__(self, *args, **kwargs):
        super(CodemirrorWidget, self).__init__(*args, **kwargs)
        self.attrs["class"] = "codemirrorEditor"
