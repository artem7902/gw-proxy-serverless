import './style.scss';
import 'bootstrap/dist/css/bootstrap.css';
import 'semantic-ui-css/semantic.min.css';

import React, {useEffect} from 'react';
import {Row, Col, Container} from 'reactstrap';

import DecisionGauge       from "../../components/decisionGauge";
import DecisionRequired    from "../../components/decisionRequired";
import InvestmentRoiTable  from "../../components/investmentRoi";
import KeyMarketsTable     from '../../components/keyMarkets';
import KeySuccess          from '../../components/keySuccess';
import MarketProductsTable from "../../components/marketProductsTable";

export default function OtWireframe5() {

  useEffect(() => {
    document.title = "Wireframe 5 (Oleg Taranenko)"
  }, []);

  return (
    <div className="App">
      <Container>
        <Row className="my-5 d-flex justify-content-between">
          <div className="title">Future Markets + Sales</div>
          <DecisionRequired notes={['', '', '']}/>
          <DecisionGauge value={250}/>
        </Row>

        <Row className="mt-4">
          <Col md={6}>
            <MarketProductsTable/>
          </Col>
          <Col md={6}>
            <div className="subtitle">Key Markets - Addressable + Trends</div>
            <KeyMarketsTable/>
            <KeySuccess/>
          </Col>
        </Row>
        <Row md={12} style={{marginTop: '50px'}}>
          <Col md={6}>
            <div className="subtitle mb-4">Product / Services</div>
            <InvestmentRoiTable/>
          </Col>
          <Col md={6}>
            <div className="subtitle mb-4">Marketing</div>
            <InvestmentRoiTable firstColumn="Initiative"/>
          </Col>
        </Row>
      </Container>
    </div>
  );
}
