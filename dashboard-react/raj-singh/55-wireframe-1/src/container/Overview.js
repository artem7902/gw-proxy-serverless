import React from 'react'
import {Container, Grid} from '@material-ui/core'
import ProgressDataTable from '../component/ProgressTable/ProgressDataTable'
import YearToDate from '../component/ProgressTable/YearToDate'  
import SpeedoMeter from '../component/SpeedoMeter/SpeedoMeter'
import './common.css'
import StackedColumnChart from '../component/stacked/StackedColumnChart'


function  Overview(){
  let criteria = [20,50,100]
	let startValue = 0
  let endValue = 100
  let rows =[ {score:10, label:"Sales, Rev, Sow, Pipeline", desc:"Decisions Resolved From Sow"},
              {score:60, label:"Key Accounts", desc:"Decisions Req"},
              {score:20, label:"Engineering", desc:"Decisions Req"},
              {score:80, label:"Future Markets + Sales", desc:"Decisions Req"},
              {score:75, label:"Finances", desc:"Decisions Req"}]

    return(
        <React.Fragment>
        <Container>
        <h1>Overview</h1>  
        <Grid container spacing={2}>         
          <Grid item xs={6}>
            <ProgressDataTable></ProgressDataTable>
          </Grid>
          <Grid item xs={6}>
            <YearToDate></YearToDate> 
        </Grid>
        </Grid>
        <Grid container spacing={2}> 
        <Grid item sm={5}  className="stackedContainer">
           <Grid container>
             <Grid item xs={12} className="revenue-stacked-chart">
              <h2>Revenue, Sow, Pipeline vs Fy TGT</h2>      
              <StackedColumnChart></StackedColumnChart>  
             </Grid>
             <Grid item xs={12} className="key-success">
              <h2>Key Successes This Month</h2> 
              <ul>
                <li></li>
                <li></li>
                <li></li>
                <li></li>
              </ul>   
             </Grid>
           </Grid>          
        </Grid>
        <Grid item sm={7} className="speedometerrow">   
        <div className="speedometerContainer">    
        <h2>Business Health</h2>
        {
          rows.map((row, index)=>{
            return(<div>
              <Grid container> 
                <Grid item xs={6} className="speedometer">      
                <SpeedoMeter isWealthResult={false} score={row.score}  healthCriteria={criteria} startValue={startValue} endValue={endValue}/>                   
                </Grid>
              <Grid item xs={6}>              
                <div className="SpeedoMeterLabel">
                  {row.label}
                </div> 
                <div className="SpeedoMeterDesc">
                 {row.desc}
                </div>               
              </Grid>
              </Grid>
            </div>
            )           
          })
        }
        </div> 
        <h3>Plus Cirrent Sheet of Budget Headlines</h3>
        </Grid>
        </Grid>
        </Container>
        </React.Fragment>
    ) 
}
export default Overview