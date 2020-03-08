import React from 'react';
import './App.css';
import ReactSpeedometer from 'react-d3-speedometer';
import LineChart from './components/lineChart';
import BarChart from './components/barChart';
import KeySuccess from './components/keySuccess';
import 'bootstrap/dist/css/bootstrap.css';
import 'semantic-ui-css/semantic.min.css';

import { Row, Col, Container } from 'reactstrap';
import { Card } from 'semantic-ui-react';

function App() {
  return (
    <div className="App">
      <Container>
        <Row className="mt-5">
          <div className="title">SALES, REVENUE, SOW + PIPELINE</div>
          <div className="ml-auto" style={{ height: 200 }}>
            <ReactSpeedometer value={500} />
          </div>
        </Row>
        <Card fluid>
          <Card.Content header="SALES" />
          <Card.Content>
            <LineChart />
          </Card.Content>
        </Card>

        <Card fluid>
          <Card.Content header="REVENUE" />
          <Card.Content>
            <LineChart revenue={true} />
          </Card.Content>
        </Card>

        <Row>
          <Col md={6}>
            <Card fluid>
              <Card.Content header="PIPELINE + SOW" />
              <Card.Content>
                <BarChart />
              </Card.Content>
            </Card>
          </Col>
          <Col md={6} className="d-flex justify-content-center">
            <KeySuccess />
          </Col>
        </Row>
      </Container>
    </div>
  );
}

export default App;
