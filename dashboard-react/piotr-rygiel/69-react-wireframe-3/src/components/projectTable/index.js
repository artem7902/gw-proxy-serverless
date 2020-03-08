import React from 'react';
import { Table } from 'semantic-ui-react';
import './style.scss';
const data = [
  'Project 1',
  'Project 2',
  'Project 3',
  'Project 4',
  'Project 5',
  'Project 6',
  'Project 7',
  'Project 8',
  'Project 9',
  'Project 10',
];
const ProjectTable = () => (
  <React.Fragment>
    <Table celled>
      <Table.Header>
        <Table.Row>
          <Table.HeaderCell>
            Project <br /> Code
          </Table.HeaderCell>
          <Table.HeaderCell>
            Project <br /> Name
          </Table.HeaderCell>
          <Table.HeaderCell>
            Client <br /> Owner
          </Table.HeaderCell>
          <Table.HeaderCell>
            Client <br /> Name
          </Table.HeaderCell>
          <Table.HeaderCell>
            Net Rev <br /> YTD
          </Table.HeaderCell>
          <Table.HeaderCell>
            % <br /> TaT
          </Table.HeaderCell>
        </Table.Row>
      </Table.Header>

      <Table.Body>
        {data.map(item => {
          return (
            <Table.Row key={item}>
              <Table.Cell>{item}</Table.Cell>
              <Table.Cell></Table.Cell>
              <Table.Cell></Table.Cell>
              <Table.Cell></Table.Cell>
              <Table.Cell></Table.Cell>
              <Table.Cell></Table.Cell>
            </Table.Row>
          );
        })}
      </Table.Body>
    </Table>
  </React.Fragment>
);

export default ProjectTable;
