import React from 'react'
import {TableContainer,TableHead, TableRow, Table, TableBody, TableCell  } from '@material-ui/core'


  
  
function createData(amount, budget, prevYear) {
    return { amount,  budget, prevYear};
  }
  
  const rows = [
    createData(500, 159, 600),
    createData(400, 237, 900)
  ];
class  DataTable extends React.Component{
    
   render(){
    return(
        <React.Fragment>       
          <TableContainer>          
          <h2>Year to Date</h2>
          <Table aria-label="simple table">
            <TableHead>
              <TableRow>
                <TableCell>£,000s</TableCell>
                <TableCell align="right">vs Budget</TableCell>
                <TableCell align="right">vs Previous Year</TableCell>
              </TableRow>
            </TableHead>
            <TableBody>
              {rows.map(row => (
                <TableRow key={row.amount}>
                  <TableCell  scope="row">
                    {row.amount}
                  </TableCell>
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