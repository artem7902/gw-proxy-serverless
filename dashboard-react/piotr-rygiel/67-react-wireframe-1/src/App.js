import React from 'react';
import './App.css';
import BusinessHealth from './components/businessHealth';
import BarChart from './components/barChart';
import KeySuccess from './components/keySuccess';
import MonthTable from './components/monthTable';
import YearTable from './components/yearTable';
import 'bootstrap/dist/css/bootstrap.css';
import 'semantic-ui-css/semantic.min.css';

import { Row, Col, Container } from 'reactstrap';
import { Card } from 'semantic-ui-react';

function App() {
  return (
    <div className="App">
      <Container>
        <Row className="my-5">
          <div className="title">OVERVIEW</div>
        </Row>
        <Row>
          <Col md={12}>
            <Card fluid>
              <Card.Content header="Progress" />
              <Card.Content>
                <Row>
                  <Col md={6}>
                    <MonthTable />
                  </Col>
                  <Col md={6}>
                    <YearTable />
                  </Col>
                </Row>
              </Card.Content>
            </Card>
          </Col>
        </Row>
        <Row className="mt-4">
          <Col md={6}>
            <Card fluid>
              <Card.Content header="Revenue, SOW + PIPELINE vs FY TqT" />
              <Card.Content>
                <BarChart />
              </Card.Content>
            </Card>
            <KeySuccess />
          </Col>
          <Col md={6}>
            <Card fluid>
              <Card.Content header="Business Health" />
              <Card.Content>
                <BusinessHealth />
              </Card.Content>
            </Card>
          </Col>
        </Row>
      </Container>
    </div>
  );
}

export default App;
