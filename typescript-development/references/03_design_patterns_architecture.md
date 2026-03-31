# TypeScript Design Patterns and Architecture

## Overview

Design patterns are reusable solutions to common software design problems. In TypeScript, these patterns leverage the type system to create robust, maintainable, and scalable applications. This guide covers essential design patterns and architectural considerations for enterprise TypeScript development.

## Design Pattern Categories

Design patterns are broadly categorized into three types:

1. **Creational Patterns**: Object creation mechanisms
2. **Structural Patterns**: Object composition and relationships
3. **Behavioral Patterns**: Object interaction and responsibility distribution

## Creational Patterns

### Singleton Pattern

**Purpose**: Ensure a class has only one instance and provide a global access point to it.

```typescript
class Database {
  private static instance: Database;
  private connection: any;

  private constructor() {
    // Private constructor prevents direct instantiation
    this.connection = this.connect();
  }

  public static getInstance(): Database {
    if (!Database.instance) {
      Database.instance = new Database();
    }
    return Database.instance;
  }

  private connect() {
    // Connection logic
    return { connected: true };
  }

  public query(sql: string): any {
    return this.connection.query(sql);
  }
}

// Usage
const db1 = Database.getInstance();
const db2 = Database.getInstance();
console.log(db1 === db2); // true - same instance
```

### Factory Pattern

**Purpose**: Create objects without specifying the exact class to create.

```typescript
interface Vehicle {
  type: string;
  drive(): void;
}

class Car implements Vehicle {
  type = "Car";
  drive(): void {
    console.log("Driving a car");
  }
}

class Truck implements Vehicle {
  type = "Truck";
  drive(): void {
    console.log("Driving a truck");
  }
}

class Motorcycle implements Vehicle {
  type = "Motorcycle";
  drive(): void {
    console.log("Riding a motorcycle");
  }
}

// Factory with type safety
class VehicleFactory {
  static createVehicle(type: "car" | "truck" | "motorcycle"): Vehicle {
    switch (type) {
      case "car":
        return new Car();
      case "truck":
        return new Truck();
      case "motorcycle":
        return new Motorcycle();
    }
  }
}

// Usage
const car = VehicleFactory.createVehicle("car");
car.drive();
```

### Factory Pattern with Generic Constraints

```typescript
interface Entity {
  id: string;
  createdAt: Date;
}

class EntityFactory<T extends Entity> {
  private idCounter = 0;

  create(data: Omit<T, "id" | "createdAt">): T {
    return {
      ...data,
      id: `${++this.idCounter}`,
      createdAt: new Date(),
    } as T;
  }
}

interface User extends Entity {
  name: string;
  email: string;
}

const userFactory = new EntityFactory<User>();
const user = userFactory.create({
  name: "John",
  email: "john@example.com",
});
```

### Builder Pattern

**Purpose**: Construct complex objects step by step.

```typescript
class User {
  constructor(
    public name: string,
    public email: string,
    public age?: number,
    public address?: string,
    public phone?: string
  ) {}
}

class UserBuilder {
  private name: string = "";
  private email: string = "";
  private age?: number;
  private address?: string;
  private phone?: string;

  setName(name: string): this {
    this.name = name;
    return this;
  }

  setEmail(email: string): this {
    this.email = email;
    return this;
  }

  setAge(age: number): this {
    this.age = age;
    return this;
  }

  setAddress(address: string): this {
    this.address = address;
    return this;
  }

  setPhone(phone: string): this {
    this.phone = phone;
    return this;
  }

  build(): User {
    return new User(this.name, this.email, this.age, this.address, this.phone);
  }
}

// Usage
const user = new UserBuilder()
  .setName("John Doe")
  .setEmail("john@example.com")
  .setAge(30)
  .setAddress("123 Main St")
  .build();
```

## Structural Patterns

### Adapter Pattern

**Purpose**: Allow incompatible interfaces to work together.

```typescript
// Old API
class OldPaymentSystem {
  processPayment(amount: number): void {
    console.log(`Processing payment of $${amount}`);
  }
}

// New interface
interface PaymentProcessor {
  pay(amount: number, currency: string): void;
}

// Adapter
class PaymentAdapter implements PaymentProcessor {
  constructor(private oldSystem: OldPaymentSystem) {}

  pay(amount: number, currency: string): void {
    // Convert and adapt
    console.log(`Currency: ${currency}`);
    this.oldSystem.processPayment(amount);
  }
}

// Usage
const oldSystem = new OldPaymentSystem();
const adapter = new PaymentAdapter(oldSystem);
adapter.pay(100, "USD");
```

### Decorator Pattern

**Purpose**: Add new functionality to objects without altering their structure.

```typescript
// Method decorator for logging
function Log(target: any, propertyKey: string, descriptor: PropertyDescriptor) {
  const originalMethod = descriptor.value;

  descriptor.value = function (...args: any[]) {
    console.log(`Calling ${propertyKey} with args:`, args);
    const result = originalMethod.apply(this, args);
    console.log(`Result:`, result);
    return result;
  };

  return descriptor;
}

// Retry decorator
function Retry(attempts: number = 3) {
  return function (
    target: any,
    propertyKey: string,
    descriptor: PropertyDescriptor
  ) {
    const originalMethod = descriptor.value;

    descriptor.value = async function (...args: any[]) {
      for (let i = 0; i < attempts; i++) {
        try {
          return await originalMethod.apply(this, args);
        } catch (error) {
          if (i === attempts - 1) throw error;
          console.log(`Retry attempt ${i + 1}`);
        }
      }
    };

    return descriptor;
  };
}

class ApiService {
  @Log
  @Retry(3)
  async fetchData(url: string): Promise<any> {
    const response = await fetch(url);
    return response.json();
  }
}
```

### Facade Pattern

**Purpose**: Provide a simplified interface to a complex subsystem.

```typescript
// Complex subsystems
class AuthenticationService {
  authenticate(username: string, password: string): boolean {
    // Complex authentication logic
    return true;
  }
}

class AuthorizationService {
  authorize(user: string, resource: string): boolean {
    // Complex authorization logic
    return true;
  }
}

class LoggingService {
  log(message: string): void {
    console.log(`[LOG] ${message}`);
  }
}

// Facade
class SecurityFacade {
  private auth = new AuthenticationService();
  private authz = new AuthorizationService();
  private logger = new LoggingService();

  login(username: string, password: string): boolean {
    this.logger.log(`Login attempt for ${username}`);
    const authenticated = this.auth.authenticate(username, password);
    if (authenticated) {
      this.logger.log(`${username} logged in successfully`);
    }
    return authenticated;
  }

  checkAccess(user: string, resource: string): boolean {
    this.logger.log(`Access check: ${user} -> ${resource}`);
    return this.authz.authorize(user, resource);
  }
}

// Usage - simple interface
const security = new SecurityFacade();
security.login("john", "password123");
security.checkAccess("john", "/admin");
```

## Behavioral Patterns

### Observer Pattern

**Purpose**: Define a one-to-many dependency between objects.

```typescript
interface Observer {
  update(data: any): void;
}

class Subject {
  private observers: Observer[] = [];

  attach(observer: Observer): void {
    this.observers.push(observer);
  }

  detach(observer: Observer): void {
    const index = this.observers.indexOf(observer);
    if (index > -1) {
      this.observers.splice(index, 1);
    }
  }

  notify(data: any): void {
    for (const observer of this.observers) {
      observer.update(data);
    }
  }
}

class ConcreteObserver implements Observer {
  constructor(private name: string) {}

  update(data: any): void {
    console.log(`${this.name} received:`, data);
  }
}

// Usage
const subject = new Subject();
const observer1 = new ConcreteObserver("Observer 1");
const observer2 = new ConcreteObserver("Observer 2");

subject.attach(observer1);
subject.attach(observer2);
subject.notify({ message: "Hello observers!" });
```

### Strategy Pattern

**Purpose**: Define a family of algorithms and make them interchangeable.

```typescript
interface PaymentStrategy {
  pay(amount: number): void;
}

class CreditCardPayment implements PaymentStrategy {
  pay(amount: number): void {
    console.log(`Paid $${amount} with credit card`);
  }
}

class PayPalPayment implements PaymentStrategy {
  pay(amount: number): void {
    console.log(`Paid $${amount} with PayPal`);
  }
}

class CryptoPayment implements PaymentStrategy {
  pay(amount: number): void {
    console.log(`Paid $${amount} with cryptocurrency`);
  }
}

class PaymentProcessor {
  constructor(private strategy: PaymentStrategy) {}

  setStrategy(strategy: PaymentStrategy): void {
    this.strategy = strategy;
  }

  processPayment(amount: number): void {
    this.strategy.pay(amount);
  }
}

// Usage
const processor = new PaymentProcessor(new CreditCardPayment());
processor.processPayment(100);

processor.setStrategy(new PayPalPayment());
processor.processPayment(200);
```

### Command Pattern

**Purpose**: Encapsulate a request as an object.

```typescript
interface Command {
  execute(): void;
  undo(): void;
}

class Light {
  turnOn(): void {
    console.log("Light is ON");
  }

  turnOff(): void {
    console.log("Light is OFF");
  }
}

class LightOnCommand implements Command {
  constructor(private light: Light) {}

  execute(): void {
    this.light.turnOn();
  }

  undo(): void {
    this.light.turnOff();
  }
}

class LightOffCommand implements Command {
  constructor(private light: Light) {}

  execute(): void {
    this.light.turnOff();
  }

  undo(): void {
    this.light.turnOn();
  }
}

class RemoteControl {
  private history: Command[] = [];

  executeCommand(command: Command): void {
    command.execute();
    this.history.push(command);
  }

  undo(): void {
    const command = this.history.pop();
    if (command) {
      command.undo();
    }
  }
}

// Usage
const light = new Light();
const remote = new RemoteControl();

remote.executeCommand(new LightOnCommand(light));
remote.executeCommand(new LightOffCommand(light));
remote.undo(); // Turns light back on
```

## Enterprise Patterns

### Dependency Injection

```typescript
// Service interfaces
interface Logger {
  log(message: string): void;
}

interface Database {
  query(sql: string): Promise<any>;
}

// Implementations
class ConsoleLogger implements Logger {
  log(message: string): void {
    console.log(`[LOG] ${message}`);
  }
}

class PostgresDatabase implements Database {
  async query(sql: string): Promise<any> {
    // Database query logic
    return [];
  }
}

// Service with dependencies
class UserService {
  constructor(
    private logger: Logger,
    private database: Database
  ) {}

  async getUser(id: string): Promise<any> {
    this.logger.log(`Fetching user ${id}`);
    return this.database.query(`SELECT * FROM users WHERE id = '${id}'`);
  }
}

// IoC Container
class Container {
  private services = new Map<string, any>();

  register<T>(name: string, instance: T): void {
    this.services.set(name, instance);
  }

  resolve<T>(name: string): T {
    return this.services.get(name);
  }
}

// Usage
const container = new Container();
container.register("logger", new ConsoleLogger());
container.register("database", new PostgresDatabase());

const userService = new UserService(
  container.resolve("logger"),
  container.resolve("database")
);
```

### Repository Pattern

```typescript
interface Repository<T> {
  findById(id: string): Promise<T | null>;
  findAll(): Promise<T[]>;
  create(entity: T): Promise<T>;
  update(id: string, entity: Partial<T>): Promise<T>;
  delete(id: string): Promise<void>;
}

interface User {
  id: string;
  name: string;
  email: string;
}

class UserRepository implements Repository<User> {
  private users: User[] = [];

  async findById(id: string): Promise<User | null> {
    return this.users.find(u => u.id === id) || null;
  }

  async findAll(): Promise<User[]> {
    return [...this.users];
  }

  async create(user: User): Promise<User> {
    this.users.push(user);
    return user;
  }

  async update(id: string, updates: Partial<User>): Promise<User> {
    const user = await this.findById(id);
    if (!user) throw new Error("User not found");
    Object.assign(user, updates);
    return user;
  }

  async delete(id: string): Promise<void> {
    const index = this.users.findIndex(u => u.id === id);
    if (index > -1) {
      this.users.splice(index, 1);
    }
  }
}
```

### Unit of Work Pattern

```typescript
class UnitOfWork {
  private newEntities: any[] = [];
  private dirtyEntities: any[] = [];
  private deletedEntities: any[] = [];

  registerNew(entity: any): void {
    this.newEntities.push(entity);
  }

  registerDirty(entity: any): void {
    this.dirtyEntities.push(entity);
  }

  registerDeleted(entity: any): void {
    this.deletedEntities.push(entity);
  }

  async commit(): Promise<void> {
    // Begin transaction
    try {
      for (const entity of this.newEntities) {
        // Insert entity
      }
      for (const entity of this.dirtyEntities) {
        // Update entity
      }
      for (const entity of this.deletedEntities) {
        // Delete entity
      }
      // Commit transaction
      this.clear();
    } catch (error) {
      // Rollback transaction
      throw error;
    }
  }

  private clear(): void {
    this.newEntities = [];
    this.dirtyEntities = [];
    this.deletedEntities = [];
  }
}
```

## Architectural Best Practices

### 1. SOLID Principles

**S - Single Responsibility Principle**
```typescript
// Bad: Multiple responsibilities
class User {
  saveToDatabase() { /* ... */ }
  sendEmail() { /* ... */ }
  generateReport() { /* ... */ }
}

// Good: Single responsibility
class User {
  constructor(public name: string, public email: string) {}
}

class UserRepository {
  save(user: User) { /* ... */ }
}

class EmailService {
  send(to: string, message: string) { /* ... */ }
}

class ReportGenerator {
  generate(user: User) { /* ... */ }
}
```

**O - Open/Closed Principle**
```typescript
// Open for extension, closed for modification
interface Shape {
  area(): number;
}

class Circle implements Shape {
  constructor(private radius: number) {}
  area(): number {
    return Math.PI * this.radius ** 2;
  }
}

class Rectangle implements Shape {
  constructor(private width: number, private height: number) {}
  area(): number {
    return this.width * this.height;
  }
}

class AreaCalculator {
  calculate(shapes: Shape[]): number {
    return shapes.reduce((sum, shape) => sum + shape.area(), 0);
  }
}
```

### 2. Modular API Layer

```typescript
// Abstract API interface
interface ApiClient {
  get<T>(url: string): Promise<T>;
  post<T>(url: string, data: any): Promise<T>;
}

// Implementation
class HttpClient implements ApiClient {
  async get<T>(url: string): Promise<T> {
    const response = await fetch(url);
    return response.json();
  }

  async post<T>(url: string, data: any): Promise<T> {
    const response = await fetch(url, {
      method: 'POST',
      body: JSON.stringify(data),
      headers: { 'Content-Type': 'application/json' }
    });
    return response.json();
  }
}

// Service layer
class UserApiService {
  constructor(private client: ApiClient) {}

  async getUsers(): Promise<User[]> {
    return this.client.get<User[]>('/api/users');
  }

  async createUser(user: Omit<User, 'id'>): Promise<User> {
    return this.client.post<User>('/api/users', user);
  }
}
```

### 3. Error Handling

```typescript
class AppError extends Error {
  constructor(
    public message: string,
    public statusCode: number,
    public isOperational: boolean = true
  ) {
    super(message);
    Object.setPrototypeOf(this, AppError.prototype);
  }
}

class NotFoundError extends AppError {
  constructor(message: string) {
    super(message, 404);
  }
}

class ValidationError extends AppError {
  constructor(message: string) {
    super(message, 400);
  }
}

// Error handler
function handleError(error: Error): void {
  if (error instanceof AppError && error.isOperational) {
    // Log and send appropriate response
    console.error(`Operational error: ${error.message}`);
  } else {
    // Critical error - log and potentially restart
    console.error(`Critical error: ${error.message}`);
    process.exit(1);
  }
}
```

## Conclusion

Design patterns and architectural principles are essential for building maintainable, scalable TypeScript applications. By leveraging TypeScript's type system alongside proven patterns, developers can create robust solutions that are easier to understand, test, and evolve. The key is to apply patterns judiciously—use them when they solve real problems, not just for the sake of using patterns.
