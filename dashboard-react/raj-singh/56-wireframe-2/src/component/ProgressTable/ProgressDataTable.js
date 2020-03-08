import React from 'react'
import {TableContainer,TableHead, TableRow, Table, TableBody, TableCell  } from '@material-ui/core'
import '../common.css'

  
  
function createData(type, amount, budget, prevYear) {
    return { type, amount, budget, prevYear};
  }
  
  const rows = [
    createData('Revenue', 1590, 300, 25),
    createData('Sales', 2370, 900, 30),
  ];
class  DataTable extends React.Component{
    
   render(){
    return(
        <React.Fragment>              
          <TableContainer>          
          <h2>Progress : This Month</h2>
          <Table aria-label="simple table">
            <TableHead>
              <TableRow>
                <TableCell> </TableCell>
                <TableCell align="right">£,000s</TableCell>
                <TableCell align="right">vs Budget</TableCell>
                <TableCell align="right">vs Previous Year</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {rows.map(row => (
                <TableRow key={row.type}>
                  <TableCell component="th" scope="row">
                    {row.type}
                  </TableCell>
                  <TableCell align="right">{row.amount}</TableCell>
                  <TableCell align="right">{row.budget}</TableCell>
                  <TableCell align="right">{row.prevYear}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
        </React.Fragment>
    )

   }   
}
export default DataTable