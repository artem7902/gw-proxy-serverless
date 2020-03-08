import React from 'react'
import {Container, Grid, Box} from '@material-ui/core'


import LineChart from '../component/Charts/LineChart'
import SalesData from '../data/sales.json'
import RevenueData from '../data/revenue.json'
import RevenueSalesData from '../data/revenue_sales.json'
import StackedChart from '../component/Charts/StackedChart'
import './common.css'
import DecisionReq from '../container/decisionReq/DecisionReq'
import KeySuccess from './keySuccess/KeySuccess'
import GaugeChart from 'react-gauge-chart'


function  Wireframe2(){  
    return(
        <React.Fragment>
          <header className="header-style">  
            <Container>            
              <Grid container>
                <Grid item xs={12}>              
                  <h2>Overview</h2> 
                </Grid>
              </Grid> 
            </Container>      
          </header>
          <Container>

          {/**        
          <Grid container spacing={2}>         
            <Grid item xs={6}>
              <ProgressDataTable></ProgressDataTable>
            </Grid>
            <Grid item xs={6}>
              <YearToDate></YearToDate> 
          </Grid>
          </Grid>  
          */}
          <Grid container> 
          <Grid item sm={12} className="padding-ad-10 sec-heading">
                <h3>Sales, Revenue, SOW + Pipeline</h3>
          </Grid>  
          <Grid item sm={12} className="stackedContainer">
            <Grid container>
              <Grid item xs={7} className="revenue-stacked-chart padding-ad-10">
                <Box className="box-style">
                  <LineChart id={1} data={SalesData}></LineChart>
                </Box>
              </Grid>
              <Grid item xs={5} className="padding-ad-10">                
                  <DecisionReq></DecisionReq> 
                  <Box className="box-style">
                    <GaugeChart id="gauge-chart" cornerRadius={0} marginInPercent={0.05} arcPadding={0} hideText={true} colors={["#ff4800", "#FFA500", "#008000"]}/>
                </Box>              
              </Grid>                        
            </Grid>          
          </Grid>             
          <Grid item sm={12} className="speedometerrow"> 
            <Grid container>          
              <Grid item xs={7} className="padding-ad-10">
                <Box className="box-style">
                <LineChart id={2} data={RevenueData}></LineChart>  
                </Box>
              </Grid> 
              <Grid item sm={5} className="padding-ad-10">                
                <KeySuccess></KeySuccess>
              </Grid>          
            </Grid>           
          </Grid>            
          <Grid item xs={12} className="pipeline-chart"> 
            <Grid container>     
              <Grid item xs={7} className="padding-ad-10">    
                <Box className="box-style">
                  <StackedChart id={2} data={RevenueSalesData}></StackedChart> 
                </Box> 
              </Grid>
              <Grid item xs={5} className="padding-ad-10"> 
              </Grid>
            </Grid>   
            </Grid> 
          </Grid>
          </Container>
        </React.Fragment>
    ) 
}
export default Wireframe2

//<h3>Plus Cirrent Sheet of Budget Headlines</h3>
/*let criteria = [20,50,100]
	let startValue = 0
  let endValue = 100
  let rows =[ {score:10, label:"Sales, Rev, Sow, Pipeline", desc:"Decisions Resolved From Sow"},
              {score:60, label:"Key Accounts", desc:"Decisions Req"},
              {score:20, label:"Engineering", desc:"Decisions Req"},
              {score:80, label:"Future Markets + Sales", desc:"Decisions Req"},
              {score:75, label:"Finances", desc:"Decisions Req"}]*/



