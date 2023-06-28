import { StyleSheet, Text, View, Image, useWindowDimensions } from 'react-native'
import LoginForm from '../components/LoginForm'
import React from 'react'
import logo from '../images/logo.jpg'

export default function Login() {
  const { height } = useWindowDimensions()
  return (
    <View style={ styles.container }>
      <Image source={ logo } style={ [styles.logo, { height: height * 0.3 }] } resizeMode='contain' />
      <LoginForm />
    </View>
  )
}

const styles = StyleSheet.create({
    container: {
      alignItems: 'center',
      padding: 30,
    },
    logo: {
      width: '70%',
    }
})