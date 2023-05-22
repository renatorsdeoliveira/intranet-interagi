/**
 * AreaView view component.
 * @module components/View/AreaView
 */

import React from 'react';
import PropTypes from 'prop-types';
import { Table } from 'semantic-ui-react';

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
      <div>
        <Table celled padded>
          <Table.Header>
            <Table.Row>
              <Table.HeaderCell singleLine>Contato</Table.HeaderCell>
              <Table.HeaderCell></Table.HeaderCell>
            </Table.Row>
          </Table.Header>
          <Table.Body>
            <Table.Row>
              <Table.Cell>E-mail</Table.Cell>
              <Table.Cell singleLine>
                {content.email ? (
                  <a href={`mailto: ${content.email}`}>{content.email}</a>
                ) : (
                  ''
                )}
              </Table.Cell>
            </Table.Row>
            <Table.Row>
              <Table.Cell>Ramal</Table.Cell>
              <Table.Cell singleLine>
                {content.ramal ? content.ramal : '-'}
              </Table.Cell>
            </Table.Row>
            <Table.Row>
              <Table.Cell>Prédio</Table.Cell>
              <Table.Cell singleLine>
                {content.predio ? content.predio.title : ''}
              </Table.Cell>
            </Table.Row>
          </Table.Body>
        </Table>
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
