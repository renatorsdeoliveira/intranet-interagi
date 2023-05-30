import RespostaView from './components/Blocks/Resposta/View';
import AreaView from './components/View/AreaView';
import PessoaView from './components/View/PessoaView';

// Icones
import exclamationSVG from '@plone/volto/icons/exclamation.svg';

const applyConfig = (config) => {
  config.settings = {
    ...config.settings,
    isMultilingual: false,
    supportedLanguages: ['pt-br'],
    defaultLanguage: 'pt-br',
  };
  config.blocks.blocksConfig.codeBlock.defaultStyle = 'light';
  config.views.contentTypesViews = {
    ...config.views.contentTypesViews,
    Area: AreaView,
    Pessoa: PessoaView,
  };

  config.blocks.blocksConfig.respostaBlock = {
    id: 'respostaBlock',
    title: 'Resposta',
    group: 'intranet',
    icon: exclamationSVG,
    view: RespostaView,
    restricted: false,
    mostUsed: false,
    sidebarTab: false,
    blockHasOwnFocusManagement: false,
  };

  config.blocks.groupBlocksOrder = [
    ...config.blocks.groupBlocksOrder,
    { id: 'intranet', title: 'Intranet' },
  ];

  return config;
};

export default applyConfig;
