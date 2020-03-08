import './style.scss';
import 'bootstrap/dist/css/bootstrap.css';
import 'semantic-ui-css/semantic.min.css';

import React                 from 'react';
import ReactSpeedometer      from 'react-d3-speedometer';
import {Row, Col, Container} from 'reactstrap';
import {Card}                from 'semantic-ui-react';

import KeySuccess       from '../../components/keySuccess';
import MetricTable      from '../../components/metricTable';
import DecisionRequired from "../../components/decisionRequired";

export default function OtWireframe6() {
  return (
    <div className="App">
      <Container>
        <Row className="my-5 d-flex justify-content-lg-between">
          <div className="title">Financials</div>
          <DecisionRequired notes={['staying', 'very very hard decision']}/>
          <ReactSpeedometer value={300} height={120} width={240}/>
        </Row>

        <Row className="mt-4">
          <Col md={6}>
            <div className="d-flex flex-column justify-content-between" style={{height: "100%"}}>
              <div className="subtitle">Headlines</div>
              <div className="subtitle mb-4">Financial Summary</div>
            </div>
          </Col>
          <Col md={6}>
            <div className="subtitle">Key Metrics</div>
            <MetricTable/>
            <KeySuccess/>
          </Col>
        </Row>
        <Row md={12}>
          <Card fluid style={{height: 500}}>
          </Card>
        </Row>
      </Container>
    </div>
  );
}
