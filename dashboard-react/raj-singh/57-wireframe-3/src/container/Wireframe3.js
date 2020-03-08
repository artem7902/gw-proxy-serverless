import React from 'react'
import {Container, Grid, Box} from '@material-ui/core'
import RevenueSalesData from '../data/revenue_sales.json'
import StackedChart from '../component/Charts/StackedChart'
import './common.css'
import DecisionReq from './decisionReq/DecisionReq'
import KeySuccess from './keySuccess/KeySuccess'
import GaugeChart from 'react-gauge-chart'
import ProgressDataTable from '../component/ProgressTable/ProgressDataTable'
import Notes from './listsOfNotes/Notes'


function  Wireframe3(){  
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
          <Grid container> 
            <Grid item sm={12} className="grid-section">           
              <Grid item xs={12} className="key-accounts padding-ad-10">
                  <h2>Key Accounts</h2>
                </Grid>
            </Grid>
          <Grid item sm={12} className="">
            <Grid container>             
            <Grid item xs={2} className="padding-ad-10">                
                             
              </Grid> 
              <Grid item xs={6} className="padding-ad-10">                
                  <DecisionReq></DecisionReq>              
              </Grid> 
              <Grid item xs={4} className="padding-ad-10">     
                  <Box className="box-style">
                    <GaugeChart id="gauge-chart" cornerRadius={0} marginInPercent={0.05} arcPadding={0} hideText={true} colors={["#ff4800", "#FFA500", "#008000"]}/>
                  </Box>   
              </Grid>                       
            </Grid>          
          </Grid>             
          <Grid item sm={12} className="stackedChart"> 
            <Grid container>          
              <Grid item xs={6} className="padding-ad-10">
                <Box className="box-style">
                  <h2>Top 10 Clients</h2>                
                  <StackedChart id={2} data={RevenueSalesData}></StackedChart>                   
                <KeySuccess></KeySuccess>
                </Box>
                  
              </Grid> 
              <Grid item sm={6} className="padding-ad-10">
                <Box className="box-style progressTable">    
                  <ProgressDataTable></ProgressDataTable>
                </Box>
              </Grid>          
            </Grid>           
          </Grid>            
          <Grid item xs={12} className="pipeline-chart"> 
            <Grid container>     
              <Grid item xs={4} className="padding-ad-10">
                <Box className="box-style b-num"> 
                  <Notes title="Issues To Be Addressed"></Notes>
                </Box>
              </Grid>
              <Grid item xs={3} className="padding-ad-10"> 
                <Box className="box-style b-alpha"> 
                  <Notes title="Finances"></Notes>
                </Box>
              </Grid>
              <Grid item xs={5} className="padding-ad-10">
                <Box className="box-style b-num"> 
                  <Notes title="New Target Clients + Action To Pursue"></Notes>
                </Box> 
              </Grid>
            </Grid>   
            </Grid> 
          </Grid>
          </Container>
        </React.Fragment>
    ) 
}
export default Wireframe3

