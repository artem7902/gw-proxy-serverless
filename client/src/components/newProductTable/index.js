import React from 'react';
import { Icon, Label, Menu, Table } from 'semantic-ui-react';

const NewProductTable = () => (
  <Table celled style={{ width: '100%' }}>
    <Table.Header>
      <Table.Row>
        <Table.HeaderCell>
          IMPROVEMENT <br /> PROJECT
        </Table.HeaderCell>
        <Table.HeaderCell>
          INVESTMENT <br /> NEEDED
        </Table.HeaderCell>
        <Table.HeaderCell>
          SPECIALTIVE <br /> VS CLIENT RECT
        </Table.HeaderCell>
      </Table.Row>
    </Table.Header>

    <Table.Body>
      <Table.Row>
        <Table.Cell>Project 1</Table.Cell>
        <Table.Cell>34.2</Table.Cell>
        <Table.Cell>48.2</Table.Cell>
      </Table.Row>
      <Table.Row>
        <Table.Cell>Project 2</Table.Cell>
        <Table.Cell>83.7</Table.Cell>
        <Table.Cell>53.4</Table.Cell>
      </Table.Row>
      <Table.Row>
        <Table.Cell>Project 3</Table.Cell>
        <Table.Cell>53.5</Table.Cell>
        <Table.Cell>36.3</Table.Cell>
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

export default NewProductTable;
