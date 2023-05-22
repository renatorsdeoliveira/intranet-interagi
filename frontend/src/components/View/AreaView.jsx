/**
 * AreaView view component.
 * @module components/View/AreaView
 */

import React from 'react';
import PropTypes from 'prop-types';

/**
 * AreaView view component class.
 * @function AreaView
 * @params {object} content Content object.
 * @returns {string} Markup of the component.
 */
const AreaView = (props) => {
  const { content } = props;

  return (
    <div id="page-document" className="ui container viewwrapper area-view">
      <header>
        <h1 className="documentFirstHeading">{content.title}</h1>
      </header>
      <div>
        <p className="description documentDescription">{content.description}</p>
      </div>
    </div>
  );
};

/**
 * Property types.
 * @property {Object} propTypes Property types.
 * @static
 */
AreaView.propTypes = {
  content: PropTypes.shape({
    title: PropTypes.string.isRequired,
    description: PropTypes.string.isRequired,
    email: PropTypes.string,
    ramal: PropTypes.string,
    predio: PropTypes.shape({
      title: PropTypes.string.isRequired,
      token: PropTypes.string.isRequired,
    }),
  }).isRequired,
};

export default AreaView;
