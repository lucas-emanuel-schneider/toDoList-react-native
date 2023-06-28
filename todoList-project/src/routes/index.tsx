import { createNativeStackNavigator} from '@react-navigation/native-stack'
import Login from '../pages/Login';

const Stack = createNativeStackNavigator();

export default function Routes() {
  return (
    <Stack.Navigator>
      <Stack.Screen name="Login" component={Login} />
    </Stack.Navigator>
  )
};