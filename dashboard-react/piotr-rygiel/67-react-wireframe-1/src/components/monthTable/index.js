import React from 'react';
import { Table } from 'semantic-ui-react';

const MonthTable = () => (
  <React.Fragment>
    <h5>This Month</h5>
    <Table celled>
      <Table.Header>
        <Table.Row>
          <Table.HeaderCell></Table.HeaderCell>
          <Table.HeaderCell>£,000s</Table.HeaderCell>
          <Table.HeaderCell>vs Budget</Table.HeaderCell>
          <Table.HeaderCell>vs Pear Yr</Table.HeaderCell>
        </Table.Row>
      </Table.Header>

      <Table.Body>
        <Table.Row>
          <Table.Cell>Revenue</Table.Cell>
          <Table.Cell>2300</Table.Cell>
          <Table.Cell>1200</Table.Cell>
          <Table.Cell>1400</Table.Cell>
        </Table.Row>
        <Table.Row>
          <Table.Cell>Sales</Table.Cell>
          <Table.Cell>1500</Table.Cell>
          <Table.Cell>600</Table.Cell>
          <Table.Cell>1100</Table.Cell>
        </Table.Row>
      </Table.Body>
    </Table>
  </React.Fragment>
);

export default MonthTable;
