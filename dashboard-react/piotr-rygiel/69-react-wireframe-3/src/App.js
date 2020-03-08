import React from 'react';
import './App.scss';
import ReactSpeedometer from 'react-d3-speedometer';

import BarChart from './components/barChart';
import KeySuccess from './components/keySuccess';
import ProjectTable from './components/projectTable';
import Note from './components/note';
import 'bootstrap/dist/css/bootstrap.css';
import 'semantic-ui-css/semantic.min.css';

import { Row, Col, Container } from 'reactstrap';
import { Card } from 'semantic-ui-react';

function App() {
  return (
    <div className="App">
      <Container>
        <Row className="my-5">
          <div className="title">Key Accounts</div>
          <div className="ml-auto" style={{ height: 150 }}>
            <ReactSpeedometer value={400} />
          </div>
        </Row>

        <Row className="mt-4">
          <Col md={6}>
            <Card fluid>
              <Card.Content header="Top 10 Clients" />
              <Card.Content>
                <BarChart />
              </Card.Content>
            </Card>
            <KeySuccess />
          </Col>
          <Col md={6}>
            <Card fluid>
              <Card.Content header="Top 10 Projects" />
              <Card.Content>
                <ProjectTable />
              </Card.Content>
            </Card>
            <div className="top-ten-projects-footer">
              <div className="top-ten-projects-label">Top Ten Subtotal</div>
              <div className="top-ten-projects-value"></div>
            </div>
            <div className="top-ten-projects-footer">
              <div className="top-ten-projects-label">All Clients Total</div>
              <div className="top-ten-projects-value"></div>
            </div>
          </Col>
        </Row>
        <Row>
          <Col md={4}>
            <Note title="Issues To Be Addressed" />
          </Col>
          <Col md={3}>
            <Note title="Finances" asc />
          </Col>
          <Col md={5}>
            <Note title="New Target Clients + Actions To Pursue" />
          </Col>
        </Row>
      </Container>
    </div>
  );
}

export default App;
