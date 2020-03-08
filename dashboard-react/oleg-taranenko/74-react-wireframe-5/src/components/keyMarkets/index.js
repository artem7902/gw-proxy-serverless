import React                      from 'react';
import {Table} from 'semantic-ui-react';
import './style.scss';

const KeyMarketsTable = ({data = [{}, {}, {}, {},]}) => (
  <React.Fragment>
    <Table celled>
      <Table.Header>
        <Table.Row>
          <Table.HeaderCell textAlign="center">
            Market
          </Table.HeaderCell>
          <Table.HeaderCell textAlign="center">
            Relevant <br/> Products
          </Table.HeaderCell>
          <Table.HeaderCell textAlign="center">
            Addressable <br/> Value
          </Table.HeaderCell>
          <Table.HeaderCell textAlign="center">
            Competition <br/> + Why Glasswall
          </Table.HeaderCell>
        </Table.Row>
      </Table.Header>

      <Table.Body>
        {data.map(({market, products, addressableValue, competition}, index) => {
          return (
            <Table.Row key={`market-${index}`}>
              <Table.Cell>{market}</Table.Cell>
              <Table.Cell>{products}</Table.Cell>
              <Table.Cell>{addressableValue}</Table.Cell>
              <Table.Cell>{competition}</Table.Cell>
            </Table.Row>
          );
        })}
      </Table.Body>
    </Table>
  </React.Fragment>
);

export default KeyMarketsTable;
