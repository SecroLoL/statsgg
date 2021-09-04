import React from 'react'
import styled from 'styled-components';
import { Link } from 'react-router-dom';

const StockContainer = styled.div`
  width: 100%;
  min-height: 6em;
  display: flex;
  border-bottom: 2px solid #d8d8d852;
  padding: 6px 8px;
  align-items: center;
`;

const Ticker = styled.h2`
  font-size: 30px;
  color: #000;
  margin-left: 10px;
  flex: 2;
  display: flex;
`;

const Name = styled.h3`
  font-size: 24px;
  color: #000;
  margin-left: 10px;
  flex: 2;
  display: flex;
`;


function StockElement(props) {
  const { ticker, name } = props;
  // Get rid of underline and increase font-size
    return (
      <Link style={{textDecoration: 'none'}} to={`/stock/${ticker}`}>
        <StockContainer>
            <span>
              <Ticker>${ticker}</Ticker>
              <Name>{name}</Name>           
            </span>
        </StockContainer>
      </Link>
    );
}

export default StockElement
