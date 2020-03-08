import React from 'react';
import { Icon, Label, Menu, Table } from 'semantic-ui-react';

const ProfitabilityTable = () => (
  <Table celled>
    <Table.Header>
      <Table.Row>
        <Table.HeaderCell>Product</Table.HeaderCell>
        <Table.HeaderCell>Margin %</Table.HeaderCell>
      </Table.Row>
    </Table.Header>

    <Table.Body>
      <Table.Row>
        <Table.Cell>Product 1</Table.Cell>
        <Table.Cell>11.21</Table.Cell>
      </Table.Row>
      <Table.Row>
        <Table.Cell>Product 2</Table.Cell>
        <Table.Cell>8.53</Table.Cell>
      </Table.Row>
      <Table.Row>
        <Table.Cell>Product 3</Table.Cell>
        <Table.Cell>4.32</Table.Cell>
      </Table.Row>
    </Table.Body>

    <Table.Footer>
      <Table.Row>
        <Table.HeaderCell colSpan="3">
          <Menu floated="right" pagination>
            <Menu.Item as="a" icon>
              <Icon name="chevron left" />
            </Menu.Item>
            <Menu.Item as="a">1</Menu.Item>
            <Menu.Item as="a">2</Menu.Item>
            <Menu.Item as="a">3</Menu.Item>
            <Menu.Item as="a">4</Menu.Item>
            <Menu.Item as="a" icon>
              <Icon name="chevron right" />
            </Menu.Item>
          </Menu>
        </Table.HeaderCell>
      </Table.Row>
    </Table.Footer>
  </Table>
);

export default ProfitabilityTable;
