define([
    'base/js/namespace',
    'jquery',
    'base/js/utils',
    'base/js/dialog'
], function(Jupyter, $, utils, dialog) {

    function make_request() {
        console.log("Cleaning notebook")
        var clean_url = utils.url_path_join(utils.get_body_data('baseUrl'), 'git/clean')
        console.log("Querying", Jupyter.notebook)
        data = {
            'name': Jupyter.notebook.notebook_name,
            'path': Jupyter.notebook.notebook_path
        }
        console.log(data);
        $.ajax({
            type: "GET",
            url: clean_url,
            data: data,
            success: function(data) {
                console.log("Data: ", data)
                dialog.modal(data)
            }
          });
    }

    function place_button() {
        if (!Jupyter.toolbar) {
            $([Jupyter.events]).on("app_initialized.NotebookApp", place_button);
            return;
        }
        Jupyter.toolbar.add_buttons_group([{
            label: 'Prepare 4',
            icon: 'fa-git',
            help: 'Hola',
            callback: make_request
        }])
    }

    function load_ipython_extension() {
        console.log("Loading");
	    place_button();
    }

    return {
	    load_ipython_extension: load_ipython_extension
    };

});