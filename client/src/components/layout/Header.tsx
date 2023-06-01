import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Container from '@mui/material/Container';
import Button from '@mui/material/Button';
import CurrencyExchangeIcon from '@mui/icons-material/CurrencyExchange';
import AccessTimeIcon from '@mui/icons-material/AccessTime';
import PsychologyAltIcon from '@mui/icons-material/PsychologyAlt';
import HomeIcon from '@mui/icons-material/Home';
import { useNavigate } from "react-router-dom";
import { GAMES } from '../../utils/constans';


export default function Header() {
    const navigate = useNavigate();


  return (
    <AppBar position="static">
      <Container maxWidth="xl">
        <Toolbar disableGutters>
          <Box sx={{ flexGrow: 1, display: { xs: 'none', md: 'flex' } }}>
            <Button key='home' sx={{ my: 2, color: 'white', display: 'block' }} onClick={()=>navigate('/')}>
                  <HomeIcon/>
                  Home
            </Button>
            <Button key={GAMES[0].name} sx={{ my: 2, color: 'white', display: 'block' }} onClick={()=>navigate(GAMES[0].url)}>
                  <PsychologyAltIcon/>{
                  GAMES[0].name}
            </Button>
            <Button key={GAMES[1].name} sx={{ my: 2, color: 'white', display: 'block' }} onClick={()=>navigate(GAMES[1].url)}>
                  <AccessTimeIcon/>
                  {GAMES[1].name}
            </Button>
            <Button key={GAMES[2].name} sx={{ my: 2, color: 'white', display: 'block' }} onClick={()=>navigate(GAMES[2].url)}>
                  <CurrencyExchangeIcon/>
                  {GAMES[2].name}
            </Button>
          </Box>
        </Toolbar>
      </Container>
    </AppBar>
  );
}
