import {
  JupyterLab, JupyterLabPlugin
} from '@jupyterlab/application';

import '../style/index.css';


/**
 * Initialization data for the jupygit-lab extension.
 */
const extension: JupyterLabPlugin<void> = {
  id: 'jupygit-lab',
  autoStart: true,
  activate: (app: JupyterLab) => {
    console.log('JupyterLab extension jupygit-lab is activated!');
  }
};

export default extension;
