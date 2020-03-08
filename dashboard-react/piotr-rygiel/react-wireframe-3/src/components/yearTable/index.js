import React from 'react';
import { Icon, Label, Menu, Table } from 'semantic-ui-react';

const YearTable = () => (
  <React.Fragment>
    <h5>Year To Date</h5>
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
          <Table.Cell>6700</Table.Cell>
          <Table.Cell>3600</Table.Cell>
          <Table.Cell>4300</Table.Cell>
        </Table.Row>
        <Table.Row>
          <Table.Cell>Sales</Table.Cell>
          <Table.Cell>4300</Table.Cell>
          <Table.Cell>2600</Table.Cell>
          <Table.Cell>3100</Table.Cell>
        </Table.Row>
      </Table.Body>
    </Table>
  </React.Fragment>
);

export default YearTable;
