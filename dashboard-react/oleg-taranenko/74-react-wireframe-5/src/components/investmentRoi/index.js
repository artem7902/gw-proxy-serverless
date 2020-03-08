import React         from 'react';
import {Table} from 'semantic-ui-react';
import './style.scss';

const InvestmentRoiTable = ({data = [{}, {}, {}, {},], firstColumn = 'New / Devt.'}) => (
  <React.Fragment>
    <Table columns={3} compact={false}>
      <Table.Header>
        <Table.Row>
          <Table.HeaderCell textAlign="center">
            {firstColumn}
          </Table.HeaderCell>
          <Table.HeaderCell textAlign="center">
            Investment
          </Table.HeaderCell>
          <Table.HeaderCell textAlign="center">
            ROI
          </Table.HeaderCell>
        </Table.Row>
      </Table.Header>

      <Table.Body>
        {data.map(({newDevelompent, investment, roi}, index) => {
          return (
            <Table.Row key={`product-${index}`}>
              <Table.Cell>{newDevelompent}</Table.Cell>
              <Table.Cell>{investment}</Table.Cell>
              <Table.Cell>{roi}</Table.Cell>
            </Table.Row>
          );
        })}
      </Table.Body>
    </Table>
  </React.Fragment>
);

export default InvestmentRoiTable;
